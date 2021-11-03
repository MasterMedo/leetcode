class Solution:
    def isNumber(self, s: str) -> bool:
        signed = number = False
        dot = dot_number = False
        e = e_signed = e_number = False

        for i, c in enumerate(s):
            if c in "-+":
                if not e:
                    if signed or number or dot:
                        return False
                    signed = True
                else:
                    if e_signed or e_number:
                        return False
                    e_signed = True

            elif c == ".":
                if dot or e:
                    return False
                dot = True

            elif c in "eE":
                if (not number and not dot_number) or e:
                    return False
                e = True

            elif c in "1234567890":
                if e:
                    e_number = True
                elif dot:
                    dot_number = True
                else:
                    number = True

            else:
                return False

        return any(
            [
                number and not dot and not e,
                dot and (number or dot_number) and not e,
                e and (number or dot_number) and e_number,
            ]
        )
