#!/usr/bin/env node

/**
 * 冒泡排序
 * @param {*} lst 
 * @returns 
 */
function bubbleSort(lst=[]) {
    if (lst.length <= 1) {
        return
    }

    for (let i = 0 ; i < (lst.length -1); i++) {
        for (let j = 0; j< (lst.length -1 - i); j++) {
            if (lst[j] > lst[j+1]) {
                const temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
            }
        }
    }
}

function index() {
    let lst = [0]
    bubbleSort(lst)
    console.log(lst)

    lst = [0, -1]
    bubbleSort(lst)
    console.log(lst)

    lst = [0, -1, 1, 2, 4, 8]
    bubbleSort(lst)
    console.log(lst)

}

index()