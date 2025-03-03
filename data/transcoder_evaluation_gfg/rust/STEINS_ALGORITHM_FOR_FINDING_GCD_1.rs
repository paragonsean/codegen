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

pub unsafe fn f_gold(mut a: i32, mut b: i32)
 -> i32 {
    if a == b { return a }
    if a == 0 as i32 { return b }
    if b == 0 as i32 { return a }
    if !a & 1 as i32 != 0 {
        if b & 1 as i32 != 0 {
            return f_gold(a >> 1 as i32, b)
        } else {
            return f_gold(a >> 1 as i32, b >> 1 as i32) <<
                       1 as i32
        }
    }
    if !b & 1 as i32 != 0 { return f_gold(a, b >> 1 as i32) }
    if a > b { return f_gold(a - b >> 1 as i32, b) }
    return f_gold(b - a >> 1 as i32, a);
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0: [i32; 10] =
        [52 as i32, 36 as i32, 12 as i32,
         69 as i32, 45 as i32, 7 as i32,
         45 as i32, 62 as i32, 96 as i32,
         89 as i32];
    let mut param1: [i32; 10] =
        [29 as i32, 94 as i32, 6 as i32,
         7 as i32, 11 as i32, 51 as i32,
         55 as i32, 86 as i32, 63 as i32,
         12 as i32];
    let mut i: i32 = 0 as i32;
    while i < param0.len() as i32 {
        if f_filled(param0[i as usize], param1[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize]) {
            n_success += 1 as i32
        }
        i += 1
    }
    println!("{} {} {} {} {}", "#Results:", " ", n_success, ", ", param0.len() as i32);
    return 0 as i32;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
