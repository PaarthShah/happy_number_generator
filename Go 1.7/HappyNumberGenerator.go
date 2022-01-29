package main

import "fmt"

const finalLength uint = 10_000

type HappyCache map[uint]bool

func sumOfSquares(num uint) uint {
	var sum uint = 0
	for num > 0 {
		digit := num % 10
		num /= 10
		sum += digit * digit
	}
	return sum
}

func isHappyBuildup(num uint) bool {
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

func isHappyCached(num uint, happyCache *HappyCache) bool {
	num = sumOfSquares(num)
	return (*happyCache)[num]
}

func main() {
	happyList := make([]uint, finalLength)
	happyCache := make(HappyCache)
	var happyCounter uint = 0
	var i uint = 1

	for ; i < 100; i++ {
		if isHappyBuildup(i) {
			happyList[happyCounter] = i
			happyCache[i] = true
			happyCounter += 1
		}
	}

	for ; happyCounter < finalLength; i++ {
		if isHappyCached(i, &happyCache) {
			happyList[happyCounter] = i
			happyCache[i] = true
			happyCounter += 1
		}
	}

	fmt.Println(happyList[finalLength-5:])
}
