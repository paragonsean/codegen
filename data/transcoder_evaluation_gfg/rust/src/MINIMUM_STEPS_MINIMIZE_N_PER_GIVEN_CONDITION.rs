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
pub unsafe extern "C" fn f_gold(mut n: libc::c_int) -> libc::c_int {
    let vla = (n + 1 as libc::c_int) as usize;
    let mut table: Vec<libc::c_int> = ::std::vec::from_elem(0, vla);
    let mut i: libc::c_int = 0 as libc::c_int;
    while i <= n { *table.as_mut_ptr().offset(i as isize) = n - i; i += 1 }
    let mut i_0: libc::c_int = n;
    while i_0 >= 1 as libc::c_int {
        if i_0 % 2 as libc::c_int == 0 {
            *table.as_mut_ptr().offset((i_0 / 2 as libc::c_int) as isize) =
                min(*table.as_mut_ptr().offset(i_0 as isize) +
                        1 as libc::c_int,
                    *table.as_mut_ptr().offset((i_0 / 2 as libc::c_int) as
                                                   isize))
        }
        if i_0 % 3 as libc::c_int == 0 {
            *table.as_mut_ptr().offset((i_0 / 3 as libc::c_int) as isize) =
                min(*table.as_mut_ptr().offset(i_0 as isize) +
                        1 as libc::c_int,
                    *table.as_mut_ptr().offset((i_0 / 3 as libc::c_int) as
                                                   isize))
        }
        i_0 -= 1
    }
    return *table.as_mut_ptr().offset(1 as libc::c_int as isize);
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut n: libc::c_int) -> libc::c_int {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0: [libc::c_int; 10] =
        [59 as libc::c_int, 7 as libc::c_int, 90 as libc::c_int,
         78 as libc::c_int, 49 as libc::c_int, 15 as libc::c_int,
         45 as libc::c_int, 56 as libc::c_int, 7 as libc::c_int,
         70 as libc::c_int];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr()) {
        if f_filled(param0[i as usize]) == f_gold(param0[i as usize]) {
            n_success += 1 as libc::c_int
        }
        i += 1
    }
    printf(b"#Results:\x00" as *const u8 as *const libc::c_char,
           b" \x00" as *const u8 as *const libc::c_char, n_success,
           b", \x00" as *const u8 as *const libc::c_char,
           len(param0.as_mut_ptr()));
    return 0 as libc::c_int;
}
#[main]
pub fn main() { unsafe { ::std::process::exit(main_0() as i32) } }
