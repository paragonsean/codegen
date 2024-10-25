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

pub unsafe fn f_gold(mut n: u32, mut d: u32)
 -> u32 {
    return n & d.wrapping_sub(1 as i32 as u32);
}
//TOFILL
unsafe fn main_0() -> i32 {
    let mut n_success: i32 = 0 as i32;
    let mut param0: [i32; 10] =
        [54 as i32, 39 as i32, 35 as i32,
         9 as i32, 62 as i32, 16 as i32,
         93 as i32, 32 as i32, 39 as i32,
         63 as i32];
    let mut param1: [i32; 10] =
        [59 as i32, 84 as i32, 81 as i32,
         60 as i32, 68 as i32, 16 as i32,
         96 as i32, 38 as i32, 62 as i32,
         16 as i32];
    let mut i: i32 = 0 as i32;
    while i < param0.len() as i32 {
        if f_filled(param0[i as usize] as u32,
                    param1[i as usize] as u32) ==
               f_gold(param0[i as usize] as u32,
                      param1[i as usize] as u32) {
            n_success += 1 as i32
        }
        i += 1
    }
    println!("{} {} {} {} {}", "#Results:", " ", n_success, ", ", param0.len() as i32);
    return 0 as i32;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
