package main

import "fmt"

const LENLIST uint = 10_000_000

// Happiness - true for happy, false for sad.
type Happiness bool

func sumOfSquares(num uint) uint {
	var sum uint = 0
	for num > 0 {
		digit := num % 10
		num /= 10
		sum += digit * digit
	}
	return sum
}

func isHappy(num uint) Happiness {
	haveSeen := map[uint]bool{
		num: true,
	}
	for num != 1 {
		num = sumOfSquares(num)
		if haveSeen[num] {
			return false
		} else {
			haveSeen[num] = true
		}
	}
	return true
}

func main() {
	happyList := make([]uint, LENLIST)
	var happyCounter uint = 0
	var i uint = 1
	for ; happyCounter < LENLIST; i++ {
		if isHappy(i) {
			happyList[happyCounter] = i
			happyCounter += 1
		}
	}
	fmt.Println(happyList[LENLIST-5:])
}
