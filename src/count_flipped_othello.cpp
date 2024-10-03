#include <iostream>
#include <random>
#include "board.hpp"

#define FULL_SEARCH_DEPTH 12
#define RANDOM_PLAY_N 10000000

void full_search(Board *board, int n_discs, uint64_t n_flipped_sum[], uint64_t n_flipped_count[]) {
    if (n_discs >= FULL_SEARCH_DEPTH + 4) {
        return;
    }
    uint64_t legal = board->get_legal();
    if (legal == 0) {
        board->pass();
            if (board->get_legal()) {
                full_search(board, n_discs, n_flipped_sum, n_flipped_count);
            }
        board->pass();
        return;
    }
    Flip flip;
    for (uint_fast8_t cell = first_bit(&legal); legal; cell = next_bit(&legal)) {
        calc_flip(&flip, board, cell);
        n_flipped_sum[n_discs] += pop_count_ull(flip.flip);
        ++n_flipped_count[n_discs];
        board->move_board(&flip);
            full_search(board, n_discs + 1, n_flipped_sum, n_flipped_count);
        board->undo_board(&flip);
    }
}

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
    Board board;
    Flip flip;

    // full search
    std::cerr << "full search until depth " << FULL_SEARCH_DEPTH << std::endl;
    board.reset();
    full_search(&board, 4, n_flipped_sum, n_flipped_count);
    
    // random play
    std::cerr << "random play N = " << RANDOM_PLAY_N << std::endl;
    std::random_device seed_gen;
    std::mt19937 engine(seed_gen());
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    for (int i = 0; i < RANDOM_PLAY_N; ++i) {
        board.reset();
        int n_discs = 4;
        while (!board.is_end()) {
            uint64_t legal = board.get_legal();
            if (legal == 0) {
                board.pass();
                legal = board.get_legal();
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
            if (n_discs >= FULL_SEARCH_DEPTH + 4) {
                n_flipped_sum[n_discs] += pop_count_ull(flip.flip);
                ++n_flipped_count[n_discs];
            }
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
    double whole_avg = 0.0;
    for (int i = 4; i < 64; ++i) {
        whole_avg += n_flipped_average[i];
    }
    whole_avg /= 60;


    std::cout << "full_search_depth " << FULL_SEARCH_DEPTH << std::endl;
    std::cout << "random_play " << RANDOM_PLAY_N << std::endl;
    for (int i = 4; i < 64; ++i) {
        std::cout << "ply " << i - 3 << " avg " << n_flipped_average[i] << " count " << n_flipped_count[i] << std::endl;
    }
    std::cout << "whole_avg " << whole_avg << std::endl;
    return 0;
}