#include <bits/stdc++.h> 
 using namespace std ;
bool canTakeDown(int bishopX, int bishopY, int pawnX, int pawnY) {
    // Check if the bishop and the pawn are on the same diagonal
    if (abs(bishopX - pawnX)!= abs(bishopY - pawnY)) {
        return false;
    }

    // Check if the bishop is in the same row or column as the pawn
    if (bishopX == pawnX || bishopY == pawnY) {
        return false;
    }

    return true;
}