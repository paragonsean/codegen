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
    #[no_mangle]
    fn memset(_: *mut libc::c_void, _: libc::c_int, _: libc::c_ulong)
     -> *mut libc::c_void;
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
pub unsafe extern "C" fn f_gold(mut f: libc::c_int, mut d: libc::c_int,
                                mut s: libc::c_int) -> libc::c_long {
    let vla = (d + 1 as libc::c_int) as usize;
    let vla_0 = (s + 1 as libc::c_int) as usize;
    let mut mem: Vec<libc::c_long> = ::std::vec::from_elem(0, vla * vla_0);
    memset(mem.as_mut_ptr() as *mut libc::c_void, 0 as libc::c_int,
           (vla * vla_0 * ::std::mem::size_of::<libc::c_long>()) as
               libc::c_ulong);
    *mem.as_mut_ptr().offset(0 as libc::c_int as isize *
                                 vla_0 as
                                     isize).offset(0 as libc::c_int as isize)
        = 1 as libc::c_int as libc::c_long;
    let mut i: libc::c_int = 1 as libc::c_int;
    while i <= d {
        let mut j: libc::c_int = i;
        while j <= s {
            *mem.as_mut_ptr().offset(i as isize *
                                         vla_0 as isize).offset(j as isize) =
                *mem.as_mut_ptr().offset(i as isize *
                                             vla_0 as
                                                 isize).offset((j -
                                                                    1 as
                                                                        libc::c_int)
                                                                   as isize) +
                    *mem.as_mut_ptr().offset((i - 1 as libc::c_int) as isize *
                                                 vla_0 as
                                                     isize).offset((j -
                                                                        1 as
                                                                            libc::c_int)
                                                                       as
                                                                       isize);
            if j - f - 1 as libc::c_int >= 0 as libc::c_int {
                *mem.as_mut_ptr().offset(i as isize *
                                             vla_0 as
                                                 isize).offset(j as isize) -=
                    *mem.as_mut_ptr().offset((i - 1 as libc::c_int) as isize *
                                                 vla_0 as
                                                     isize).offset((j - f -
                                                                        1 as
                                                                            libc::c_int)
                                                                       as
                                                                       isize)
            }
            j += 1
        }
        i += 1
    }
    return *mem.as_mut_ptr().offset(d as isize *
                                        vla_0 as isize).offset(s as isize);
}
#[no_mangle]
pub unsafe extern "C" fn f_filled(mut f: libc::c_int, mut d: libc::c_int,
                                  mut s: libc::c_int) -> libc::c_long {
    panic!("Reached end of non-void function without returning");
}
unsafe fn main_0() -> libc::c_int {
    let mut n_success: libc::c_int = 0 as libc::c_int;
    let mut param0: [libc::c_int; 10] =
        [57 as libc::c_int, 58 as libc::c_int, 38 as libc::c_int,
         5 as libc::c_int, 91 as libc::c_int, 76 as libc::c_int,
         38 as libc::c_int, 97 as libc::c_int, 97 as libc::c_int,
         99 as libc::c_int];
    let mut param1: [libc::c_int; 10] =
        [5 as libc::c_int, 45 as libc::c_int, 89 as libc::c_int,
         39 as libc::c_int, 90 as libc::c_int, 56 as libc::c_int,
         43 as libc::c_int, 26 as libc::c_int, 90 as libc::c_int,
         2 as libc::c_int];
    let mut param2: [libc::c_int; 10] =
        [33 as libc::c_int, 4 as libc::c_int, 9 as libc::c_int,
         30 as libc::c_int, 47 as libc::c_int, 46 as libc::c_int,
         84 as libc::c_int, 52 as libc::c_int, 90 as libc::c_int,
         26 as libc::c_int];
    let mut i: libc::c_int = 0 as libc::c_int;
    while i < len(param0.as_mut_ptr()) {
        if f_filled(param0[i as usize], param1[i as usize],
                    param2[i as usize]) ==
               f_gold(param0[i as usize], param1[i as usize],
                      param2[i as usize]) {
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
