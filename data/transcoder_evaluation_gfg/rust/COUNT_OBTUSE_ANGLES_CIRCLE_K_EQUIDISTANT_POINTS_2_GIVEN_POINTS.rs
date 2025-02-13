#![feature(main)]
// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

#[no_mangle]
pub unsafe fn abs(mut x: i32)
 -> i32 {
    return x.abs();
}

#[no_mangle]
pub unsafe fn min(mut x: i32, mut y: i32)
 -> i32 {
    return if x < y { x } else { y };
}
#[no_mangle]
pub unsafe fn max(mut x: i32, mut y: i32)
 -> i32 {
    return if x > y { x } else { y };
}

pub unsafe fn f_gold(mut a: i32, mut b: i32,
                                mut k: i32) -> i32 {
    let mut c1: i32 = b - a - 1 as i32;
    let mut c2: i32 = k - b + (a - 1 as i32);
    if c1 == c2 { return 0 as i32 }
    return min(c1, c2);
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0: [i32; 10] =
        [83 as i32, 3 as i32, 11 as i32,
         50 as i32, 40 as i32, 62 as i32,
         40 as i32, 66 as i32, 6 as i32,
         25 as i32];
    let mut param1: [i32; 10] =
        [98 as i32, 39 as i32, 96 as i32,
         67 as i32, 16 as i32, 86 as i32,
         78 as i32, 11 as i32, 9 as i32,
         5 as i32];
    let mut param2: [i32; 10] =
        [86 as i32, 87 as i32, 30 as i32,
         48 as i32, 32 as i32, 76 as i32,
         71 as i32, 74 as i32, 19 as i32,
         5 as i32];
    let mut i: i32 = 0 as i32;
    while i < param0.len() as i32 {
        if f_filled(param0[i as usize], param1[i as usize],
                    param2[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize],
                      param2[i as usize]) {
            n_success += 1 as i32
        }
        i += 1
    }
    println!("{} {} {} {} {}", "#Results:", " ", n_success, ", ", param0.len() as i32);
    return 0 as i32;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
