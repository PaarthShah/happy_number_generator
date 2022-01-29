package main

import (
	"fmt"
)

func sumOfSquares(num uint) uint {
	var sum uint = 0
	for num > 0 {
		digit := num % 10
		num /= 10
		sum += digit * digit
	}
	return sum
}

func isHappy(num uint) bool {
	haveSeen := map[uint]bool{
		num: true,
	}
	for num != 1 {
		num = sumOfSquares(num)
		if haveSeen[num] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isHappy(7))
	fmt.Println(isHappy(4))
}
