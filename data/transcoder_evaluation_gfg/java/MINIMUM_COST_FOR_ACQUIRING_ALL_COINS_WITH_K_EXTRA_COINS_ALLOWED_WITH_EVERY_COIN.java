// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;
import javafx.util.Pair;
public class MINIMUM_COST_FOR_ACQUIRING_ALL_COINS_WITH_K_EXTRA_COINS_ALLOWED_WITH_EVERY_COIN{
static int f_gold ( int coin [ ] , int n , int k ) {
  Arrays . sort ( coin ) ;
  int coins_needed = ( int ) Math . ceil ( 1.0 * n / ( k + 1 ) ) ;
  int ans = 0 ;
  for ( int i = 0 ;
  i <= coins_needed - 1 ;
  i ++ ) ans += coin [ i ] ;
  return ans ;
}


//TOFILL

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{2,4,5,9,10,10,11,14,15,19,21,22,29,36,36,38,39,39,39,41,41,42,45,45,48,55,56,57,64,66,66,66,66,69,74,76,80,81,82,82,85,87,95,95});
    param0.add(new int[]{-6,-52,20,-98,-10,48,36,66,-88,94,68,16});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{91,62,29,49,6,11,10,43,78,35,32,5,1,48,15,24,4,71});
    param0.add(new int[]{-98,-92,-88,-84,-82,-78,-74,-74,-68,-62,-62,-56,-56,-50,-46,-44,-26,-18,-14,-8,-8,-6,8,16,20,20,22,26,36,42,44,44,52,60,66,68,68,70,76,84});
    param0.add(new int[]{1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,1,0});
    param0.add(new int[]{5,12,38,39,52,54,62,81,87,93});
    param0.add(new int[]{86,-18,-32,70,40,-76,-8,8,-84,-10,92,94,-18,-12,-26,-40,-74,60,16,-70,44,-32,40,-24,0,4});
    param0.add(new int[]{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1});
    param0.add(new int[]{86,62,98,97,61,31,23,56,63,72,44,74,58,97});
    List<Integer> param1 = new ArrayList<>();
    param1.add(33);
    param1.add(6);
    param1.add(16);
    param1.add(13);
    param1.add(25);
    param1.add(32);
    param1.add(6);
    param1.add(25);
    param1.add(37);
    param1.add(12);
    List<Integer> param2 = new ArrayList<>();
    param2.add(27);
    param2.add(10);
    param2.add(16);
    param2.add(17);
    param2.add(34);
    param2.add(32);
    param2.add(8);
    param2.add(20);
    param2.add(29);
    param2.add(13);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i),param2.get(i)) == f_gold(param0.get(i),param1.get(i),param2.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}