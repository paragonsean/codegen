#![allow(dead_code, mutable_transmutes, non_camel_case_types, non_snake_case,
         non_upper_case_globals, unused_assignments, unused_mut)]
#![register_tool(c2rust)]
#![feature(main, register_tool)]
extern "C" {
    #[no_mangle]
    fn printf(_: *const libc::c_char, _: ...) -> libc::c_int;
    #[no_mangle]
    fn qsort(__base: *mut libc::c_void, __nmemb: size_t, __size: size_t,
             __compar: __compar_fn_t);
}
pub type size_t = libc::c_ulong;
pub type __compar_fn_t
    =
    Option<unsafe extern "C" fn(_: *const libc::c_void,
                                _: *const libc::c_void) -> libc::c_int>;
// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//
#[no_mangle]
pub unsafe extern "C" fn min(mut x: libc::c_int, mut y: libc::c_int)
 -> libc::c_int {
    return if x < y { x } else { y };
}
#[no_mangle]
pub unsafe extern "C" fn max(mut x: libc::c_int, mut y: libc::c_int)
 -> libc::c_int {
    return if x > y { x } else { y };
}
#[no_mangle]
pub unsafe extern "C" fn cmpfunc(mut a: *const libc::c_void,
                                 mut b: *const libc::c_void) -> libc::c_int {
    return *(a as *mut libc::c_int) - *(b as *mut libc::c_int);
}
#[no_mangle]
pub unsafe extern "C" fn len(mut arr: *mut libc::c_int) -> libc::c_int {
    return (::std::mem::size_of::<*mut libc::c_int>() as
                libc::c_ulong).wrapping_div(::std::mem::size_of::<libc::c_int>()
                                                as libc::c_ulong) as
               libc::c_int;
}
#[no_mangle]
pub unsafe extern "C" fn sort(mut arr: *mut libc::c_int, mut n: libc::c_int) {
    qsort(arr as *mut libc::c_void, n as size_t,
          ::std::mem::size_of::<libc::c_int>() as libc::c_ulong,
          Some(cmpfunc as
                   unsafe extern "C" fn(_: *const libc::c_void,
                                        _: *const libc::c_void)
                       -> libc::c_int));
}
#[no_mangle]
pub unsafe extern "C" fn f_gold(mut arr: *mut libc::c_int, mut n: libc::c_int,
                                mut k: libc::c_int) -> bool {
    let mut count: libc::c_int = 0;
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < n {
        count = 0 as libc::c_int;
        let mut j: libc::c_int = 0 as libc::c_int;
        while j < n {
            if *arr.offset(j as isize) == *arr.offset(i as isize) {
                count += 1
            }
            if count > 2 as libc::c_int * k { return 0 as libc::c_int != 0 }
            j += 1
        }
        i += 1
    }
    return 1 as libc::c_int != 0;
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut arr: *mut libc::c_int,
                                  mut n: libc::c_int, mut k: libc::c_int)
 -> bool {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0_0: [libc::c_int; 5] =
        [1 as libc::c_int, 1 as libc::c_int, 2 as libc::c_int,
         3 as libc::c_int, 1 as libc::c_int];
    let mut param0_1: [libc::c_int; 6] =
        [2 as libc::c_int, 3 as libc::c_int, 3 as libc::c_int,
         5 as libc::c_int, 3 as libc::c_int, 3 as libc::c_int];
    let mut param0_2: [libc::c_int; 5] =
        [0 as libc::c_int, 0 as libc::c_int, 1 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int];
    let mut param0_3: [libc::c_int; 28] =
        [7 as libc::c_int, 60 as libc::c_int, 78 as libc::c_int,
         91 as libc::c_int, 80 as libc::c_int, 75 as libc::c_int,
         85 as libc::c_int, 21 as libc::c_int, 41 as libc::c_int,
         63 as libc::c_int, 1 as libc::c_int, 84 as libc::c_int,
         69 as libc::c_int, 13 as libc::c_int, 94 as libc::c_int,
         25 as libc::c_int, 54 as libc::c_int, 54 as libc::c_int,
         52 as libc::c_int, 68 as libc::c_int, 53 as libc::c_int,
         35 as libc::c_int, 17 as libc::c_int, 37 as libc::c_int,
         98 as libc::c_int, 27 as libc::c_int, 2 as libc::c_int,
         31 as libc::c_int];
    let mut param0_4: [libc::c_int; 27] =
        [-(96 as libc::c_int), -(94 as libc::c_int), -(82 as libc::c_int),
         -(80 as libc::c_int), -(78 as libc::c_int), -(66 as libc::c_int),
         -(36 as libc::c_int), -(24 as libc::c_int), -(18 as libc::c_int),
         -(12 as libc::c_int), -(2 as libc::c_int), -(2 as libc::c_int),
         6 as libc::c_int, 8 as libc::c_int, 10 as libc::c_int,
         12 as libc::c_int, 36 as libc::c_int, 38 as libc::c_int,
         42 as libc::c_int, 58 as libc::c_int, 64 as libc::c_int,
         68 as libc::c_int, 82 as libc::c_int, 84 as libc::c_int,
         86 as libc::c_int, 88 as libc::c_int, 94 as libc::c_int];
    let mut param0_5: [libc::c_int; 45] =
        [0 as libc::c_int, 1 as libc::c_int, 1 as libc::c_int,
         1 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 1 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         1 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int, 1 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int, 1 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         0 as libc::c_int, 1 as libc::c_int, 0 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int, 0 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int, 0 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 1 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 1 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int, 0 as libc::c_int];
    let mut param0_6: [libc::c_int; 16] =
        [16 as libc::c_int, 19 as libc::c_int, 25 as libc::c_int,
         25 as libc::c_int, 32 as libc::c_int, 37 as libc::c_int,
         48 as libc::c_int, 59 as libc::c_int, 60 as libc::c_int,
         60 as libc::c_int, 71 as libc::c_int, 74 as libc::c_int,
         77 as libc::c_int, 81 as libc::c_int, 91 as libc::c_int,
         94 as libc::c_int];
    let mut param0_7: [libc::c_int; 30] =
        [-(62 as libc::c_int), -(94 as libc::c_int), 72 as libc::c_int,
         -(22 as libc::c_int), 86 as libc::c_int, -(80 as libc::c_int),
         64 as libc::c_int, 98 as libc::c_int, -(82 as libc::c_int),
         -(50 as libc::c_int), 12 as libc::c_int, -(4 as libc::c_int),
         56 as libc::c_int, 46 as libc::c_int, -(80 as libc::c_int),
         2 as libc::c_int, -(86 as libc::c_int), -(44 as libc::c_int),
         -(26 as libc::c_int), 68 as libc::c_int, -(94 as libc::c_int),
         -(82 as libc::c_int), 74 as libc::c_int, 26 as libc::c_int,
         94 as libc::c_int, 40 as libc::c_int, 50 as libc::c_int,
         -(40 as libc::c_int), -(42 as libc::c_int), -(10 as libc::c_int)];
    let mut param0_8: [libc::c_int; 8] =
        [0 as libc::c_int, 0 as libc::c_int, 0 as libc::c_int,
         0 as libc::c_int, 0 as libc::c_int, 1 as libc::c_int,
         1 as libc::c_int, 1 as libc::c_int];
    let mut param0_9: [libc::c_int; 35] =
        [83 as libc::c_int, 57 as libc::c_int, 2 as libc::c_int,
         47 as libc::c_int, 70 as libc::c_int, 22 as libc::c_int,
         49 as libc::c_int, 51 as libc::c_int, 25 as libc::c_int,
         57 as libc::c_int, 32 as libc::c_int, 7 as libc::c_int,
         8 as libc::c_int, 99 as libc::c_int, 6 as libc::c_int,
         86 as libc::c_int, 24 as libc::c_int, 79 as libc::c_int,
         42 as libc::c_int, 43 as libc::c_int, 1 as libc::c_int,
         24 as libc::c_int, 68 as libc::c_int, 11 as libc::c_int,
         24 as libc::c_int, 12 as libc::c_int, 43 as libc::c_int,
         40 as libc::c_int, 14 as libc::c_int, 45 as libc::c_int,
         11 as libc::c_int, 46 as libc::c_int, 12 as libc::c_int,
         80 as libc::c_int, 66 as libc::c_int];
    let mut param0: [*mut libc::c_int; 10] =
        [param0_0.as_mut_ptr(), param0_1.as_mut_ptr(), param0_2.as_mut_ptr(),
         param0_3.as_mut_ptr(), param0_4.as_mut_ptr(), param0_5.as_mut_ptr(),
         param0_6.as_mut_ptr(), param0_7.as_mut_ptr(), param0_8.as_mut_ptr(),
         param0_9.as_mut_ptr()];
    let mut param1: [libc::c_int; 10] =
        [5 as libc::c_int, 6 as libc::c_int, 2 as libc::c_int,
         24 as libc::c_int, 24 as libc::c_int, 34 as libc::c_int,
         10 as libc::c_int, 20 as libc::c_int, 5 as libc::c_int,
         21 as libc::c_int];
    let mut param2: [libc::c_int; 10] =
        [2 as libc::c_int, 2 as libc::c_int, 1 as libc::c_int,
         2 as libc::c_int, 3 as libc::c_int, 2 as libc::c_int,
         8 as libc::c_int, 4 as libc::c_int, 2 as libc::c_int,
         33 as libc::c_int];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr() as *mut libc::c_int) {
        if f_filled(param0[i as usize], param1[i as usize],
                    param2[i as usize]) as libc::c_int ==
               f_gold(param0[i as usize], param1[i as usize],
                      param2[i as usize]) as libc::c_int {
            n_success += 1 as libc::c_int
        }
        i += 1
    }
    printf(b"#Results:\x00" as *const u8 as *const libc::c_char,
           b" \x00" as *const u8 as *const libc::c_char, n_success,
           b", \x00" as *const u8 as *const libc::c_char,
           len(param0.as_mut_ptr() as *mut libc::c_int));
    return 0 as libc::c_int;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
