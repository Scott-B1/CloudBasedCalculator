package main

import (
  "testing"
)

func TestSquare(t *testing.T) {
	answer := Squared(3)
	if answer != 9 {
		t.Errorf("Squaring is incorrect, Received: %d, Expected: %d", answer, 9)
	}
}

func TestSquareNegative(t *testing.T) {
	answer := Squared(-2)
	if answer != 4 {
		t.Errorf("Squaring is incorrect, Received: %d, Expected: %d", answer, 4)
	}
}
