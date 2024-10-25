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
                                mut d: i32) -> i32 {
    let mut temp: i32 = a;
    a = min(a, b);
    b = max(temp, b);
    if d >= b { return (d + b - 1 as i32) / b }
    if d == 0 as i32 { return 0 as i32 }
    if d == a { return 1 as i32 }
    return 2 as i32;
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0: [i32; 10] =
        [35 as i32, 85 as i32, 22 as i32,
         8 as i32, 12 as i32, 58 as i32,
         65 as i32, 10 as i32, 23 as i32,
         5 as i32];
    let mut param1: [i32; 10] =
        [8 as i32, 55 as i32, 23 as i32,
         43 as i32, 64 as i32, 25 as i32,
         4 as i32, 95 as i32, 13 as i32,
         50 as i32];
    let mut param2: [i32; 10] =
        [77 as i32, 33 as i32, 64 as i32,
         29 as i32, 11 as i32, 26 as i32,
         28 as i32, 55 as i32, 54 as i32,
         71 as i32];
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
