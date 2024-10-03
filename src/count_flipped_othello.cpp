#include <iostream>
#include <random>
#include "board.hpp"

#define N 10000000

int main() {
    bit_init();
    mobility_init();
    flip_init();
    uint64_t n_flipped_sum[64];
    uint64_t n_flipped_count[64];
    for (int i = 0; i < 64; ++i) {
        n_flipped_sum[i] = 0;
        n_flipped_count[i] = 0;
    }
    std::random_device seed_gen;
    std::mt19937 engine(seed_gen());
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    for (int i = 0; i < N; ++i) {
        Board board;
        Flip flip;
        board.reset();
        int n_discs = 4;
        while (!board.is_end()) {
            uint64_t legal = board.get_legal();
            if (legal == 0) {
                board.pass();
                continue;
            }
            int n_legal = pop_count_ull(legal);
            int used_legal_idx = (int)(dist(engine) * n_legal);
            if (n_legal <= used_legal_idx) {
                std::cerr << "ERR " << n_legal << " " << used_legal_idx << std::endl;
            }
            for (int j = 0; j < used_legal_idx; ++j) {
                legal &= legal - 1;
            }
            if (legal == 0) {
                std::cerr << "ERR2 " << n_legal << " " << used_legal_idx << std::endl;
            }
            int policy = first_bit(&legal);
            calc_flip(&flip, &board, policy);
            n_flipped_sum[n_discs] += pop_count_ull(flip.flip);
            ++n_flipped_count[n_discs];
            board.move_board(&flip);
            ++n_discs;
        }
    }
    double n_flipped_average[64];
    for (int i = 0; i < 64; ++i) {
        if (n_flipped_count[i] == 0) {
            n_flipped_average[i] = 0;
        } else {
            n_flipped_average[i] = (double)n_flipped_sum[i] / n_flipped_count[i];
        }
    }
    double avg = 0.0;
    for (int i = 4; i < 64; ++i) {
        avg += n_flipped_average[i];
    }
    avg /= 60;
    std::cerr << "played " << N << " games randomly" << std::endl;
    for (int i = 0; i < 64; ++i) {
        std::cout << n_flipped_average[i] << " ";
        if (i % 8 == 7) {
            std::cout << "\n";
        }
    }
    std::cout << "avg " << avg << std::endl;
    return 0;
}