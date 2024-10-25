// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;
int f_gold ( int s ) {
  int sum = 0;
  for ( int n = 1;
  sum < s;
  n ++ ) {
    sum += n * n * n;
    if ( sum == s ) return n;
  }
  return - 1;
}


//TOFILL

int main() {
    int n_success = 0;
    vector<int> param0 {15,36,39,43,75,49,56,14,62,97};
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0[i]) == f_gold(param0[i]))
        {
            n_success+=1;
        }
    }
    cout << "#Results:" << " " << n_success << ", " << param0.size();
    return 0;
}