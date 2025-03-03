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

int f_gold ( string & str ) {
  int n = strlen(str);
  int res = - 1;
  for ( int i = 0;
  i < n - 1;
  i ++ ) for ( int j = i + 1;
  j < n;
  j ++ ) if ( str [ i ] == str [ j ] ) res = max ( res, abs ( j - i - 1 ) );
  return res;
}


int f_filled ( string & str ) {}

int main(void) {
    int n_success = 0;
    char param0[][100] = {"cI","76478","1","tr","10","01","Rmhzp","5784080133917","1100","OK"};
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