// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//


#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

int min(int x, int y) { return (x < y)? x: y; }
int max(int x, int y) { return (x > y)? x: y; }
int cmpfunc (const void * a, const void * b) {return ( *(int*)a - *(int*)b );}
int len (int arr [ ]) {return ((int) (sizeof (arr) / sizeof (arr)[0]));}
void sort (int arr [ ], int n) {qsort (arr, n, sizeof(int), cmpfunc);}

int f_gold ( int n ) {
  int A [ n + 1 ], B [ n + 1 ];
  A [ 0 ] = 1, A [ 1 ] = 0, B [ 0 ] = 0, B [ 1 ] = 1;
  for ( int i = 2;
  i <= n;
  i ++ ) {
    A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ];
    B [ i ] = A [ i - 1 ] + B [ i - 2 ];
  }
  return A [ n ];
}


int f_filled ( int n ) {}

int main(void) {
    int n_success = 0;
    int param0[] = {29,13,25,65,27,42,19,50,59,13};
    for(int i = 0; i < len(param0); ++i)
    {
        if(f_filled(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    printf("#Results:", " ", n_success, ", ", len(param0));
    return 0;
}