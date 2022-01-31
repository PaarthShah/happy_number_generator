package main

import "fmt"
import "sync"

const finalLength uint = 100_000
const workerCount int = 8

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

func isHappyCached(numbers <-chan uint, happyCache *sync.Map, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range numbers {
		newNum := sumOfSquares(num)
		_, isHappy := (*happyCache).Load(newNum)
		if isHappy {
			(*happyCache).Store(num, true)
		}
	}
}

func main() {
	happyList := make([]uint, finalLength)
	var happyCache sync.Map
	var happyCounter uint = 0
	var i uint = 1 // Main iterator through the whole numbers.

	for ; i < 1000; i++ {
		if isHappyBuildup(i) {
			happyCache.Store(i, true)
		}
	}

	numbers := make(chan uint, finalLength*10)

	for ; i < finalLength*10; i++ {
		numbers <- i
	}
	close(numbers)

	wg := new(sync.WaitGroup)
	wg.Add(workerCount)

	for x := 0; x < workerCount; x++ {
		go isHappyCached(numbers, &happyCache, wg)
	}
	wg.Wait()

	for i = 1; happyCounter < finalLength; i++ {
		_, isHappy := happyCache.Load(i)
		if isHappy {
			happyList[happyCounter] = i
			happyCounter++
		}
	}

	fmt.Println(happyList[finalLength-5:])
}
