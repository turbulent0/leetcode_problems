class Solution(object):
    def read(self, buf, n):
        """
        at first copy to buf4 every 4 chars, then copy to buf (for better memory usage)
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        read4(buf4) reads 4 characters at a time from a file, then copy to buf4
        buf4 is a list of 4 chars
        buf is a list of n chars
        """

        count = 0
        buf4 = [''] * 4
        n_char_copy = 0
        while(n > 0):

            count = min(read4(buf4), n)
            for i in range(count):
                buf[n_char_copy] = buf4[i]
                n_char_copy += 1
            n -= 4
        print(buf4, buf)
        return n_char_copy