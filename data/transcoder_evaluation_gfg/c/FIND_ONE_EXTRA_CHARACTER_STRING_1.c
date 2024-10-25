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

char f_gold ( char strA [], char strB [] ) {
  int res = 0, i;
  for ( i = 0;
  i < strlen(strA);
  i ++ ) {
    res ^= strA [ i ];
  }
  for ( i = 0;
  i < strlen(strB);
  i ++ ) {
    res ^= strB [ i ];
  }
  return ( ( char ) ( res ) );
}


char f_filled ( char strA [], char strB [] ) {}

int main(void) {
    int n_success = 0;
    char param0[][100] = {"obfLA mmMYvghH","2941","0111111","oWvbFstI","4937516500","101110100","hYZscJQFBE","58443","1100","ZUdYuIBVNaeeb"};
    char param1[][100] = {"obfLA  mmMYvghH","23941","01011111","oWvsbFstI","49376516500","1011210100","hYZscJQQFBE","584443","11000","ZUdYVuIBVNaeeb"};
    for(int i = 0; i < len(param0); ++i)
    {
        if(f_filled(param0[i],param1[i]) == f_gold(param0[i],param1[i]))
        {
            n_success+=1;
        }
    }
    printf("#Results:", " ", n_success, ", ", len(param0));
    return 0;
}