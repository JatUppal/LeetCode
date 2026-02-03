class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            chars[write] = chars[read]
            write += 1
            count = 0
            curr = chars[read]
            while read < len(chars) and chars[read] == curr:
                count += 1
                read += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write