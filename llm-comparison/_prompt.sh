#!/bin/bash

puzzle_number=$1

if [[ -z "$puzzle_number" || "$puzzle_number" -lt 0 || "$puzzle_number" -gt 9 ]]; then
  echo "Usage: $0 <puzzle_number (0-9)>"
  exit 1
fi

puzzle_line=$(sed -n "$((puzzle_number + 1))p" _inputs.csv)

if [[ -z "$puzzle_line" ]]; then
  echo "Error: Puzzle number $puzzle_number not found in _inputs.csv"
  exit 1
fi

prompt="You are an expert Connections puzzle solver. Your task is to analyze the following 16 words and group them into four categories of four.

Here are the words: $puzzle_line

Here are some tips to help you solve the puzzle:

1. **Start with the Obvious:** Look for the easiest categories first. Often, there will be a group of four words that clearly belong together.
2. **Look for Synonyms and Related Concepts:** Consider words that have similar meanings or are associated with the same topic.
3. **Think Outside the Box:** Some categories might be based on wordplay, puns, or less obvious connections.
4. **Consider Multiple Meanings:** Some words might have multiple meanings, and the category might be based on a less common meaning.
5. **Check for Common Patterns:** Look for patterns like all words starting with the same letter, all words being a type of something (e.g., types of fruit), or all words having a similar sound.
6. **Eliminate and Group:** As you identify categories, remove the words from the pool and focus on the remaining words.
7. **Sanity Check:** Once you have your four categories, double-check that each group of four words makes logical sense together. Ensure there are no nonsensical pairings.

Your response should be formatted as follows, with comma-separated values for each category:

Word1,Word2,Word3,Word4,Word1,Word2,Word3,Word4,Word1,Word2,Word3,Word4,Word1,Word2,Word3,Word4"

echo "$prompt" | pbcopy