'''

Parses words_alpha into a dictionary-tree structure where nodes are keys (as
individual letters) and values are dictionaries of further nodes. Each path from
the root in this tree represents one word in the dictionary. There is no
indication (yet) of whether each letter in a path is a complete word in and of
itself.

'''

import unittest

root = {}
def add_word_to_root(root, word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}

        node = node[char]

    return root

def main():
    INPUT_FILE = "words_alpha.txt"
    with open(INPUT_FILE, "r") as words:
        root = {}
        for word in words.readlines():
            print(word.strip("\n"))
            root = add_word_to_root()

class Tests(unittest.TestCase):

    def test_add_word_single(self):
        tree = {}
        add_word_to_root(tree, "abc")
        self.assertEqual(tree, {"a":{"b":{"c":{}}}})

    def test_add_word_double(self):
        tree = {}
        add_word_to_root(tree, "abc")
        add_word_to_root(tree, "xyz")

        expected = {
                "a": {
                    "b": {
                        "c": {}
                        }
                    },
                "x": {
                    "y": {
                        "z": {}
                        }
                    }
                }

        self.assertEqual(tree, expected)

    def test_add_word_overlapping(self):
        tree = {}

        add_word_to_root(tree, "ab")
        add_word_to_root(tree, "abcd")

        expected = {"a":{"b":{"c":{"d":{}}}}}

        self.assertEqual(tree, expected)

    def test_add_word_diverging(self):
        tree = {}

        add_word_to_root(tree, "ab")
        add_word_to_root(tree, "ac")

        expected = {"a": {"b":{}, "c":{}}}

        self.assertEqual(tree, expected)

    def test_empty_word(self):
        tree = {}

        add_word_to_root(tree, "")

        self.assertEqual(tree, {})

    def test_add_word_to_existing(self):

        existing = {
                "a": {
                    "b": {}
                    }
                }

        add_word_to_root(existing, "abc")

        expected = {
                "a": {
                    "b": {
                        "c": {}
                        }
                    }
                }

        self.assertEqual(existing, expected)

if __name__ == "__main__":
    unittest.main()
    main()
