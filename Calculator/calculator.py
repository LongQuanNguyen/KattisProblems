def clean_line(line):
    return line.replace(" ", "")


def read_digit(string, start_idx):
    end_idx = start_idx
    while end_idx < len(string) and string[end_idx].isdigit():
        end_idx += 1
    return string[start_idx: end_idx], end_idx


def check_negative_num(string, idx):
    if string[idx] != "-":
        return False
    if idx == 0:
        return True
    return string[idx - 1] in "(*/+-"


def is_stack_op_higher_equal_precedence(stack_op, incoming_op):
    precedence = {"*": 2, "/": 2, "+": 1, "-": 1}
    operators = "+-/*"
    return (
        stack_op in operators and
        incoming_op in operators and
        precedence[stack_op] >= precedence[incoming_op]
    )


def convert_rpn(line):
    stack = list()
    queue = list()

    i = 0
    while i < len(line):
        if line[i].isdigit():
            number, next_idx = read_digit(line, i)
            queue.append(number)
            i = next_idx - 1
        elif line[i] == "(":
            stack.append(line[i])
        elif line[i] == ")":
            stack_item = stack.pop()
            while stack_item != "(":
                queue.append(stack_item)
                stack_item = stack.pop()
        elif line[i] == "-" and check_negative_num(line, i):
            number, next_idx = read_digit(line, i + 1)
            queue.append("-" + number)
            i = next_idx - 1
        else:
            while len(stack) > 0 and is_stack_op_higher_equal_precedence(stack[-1], line[i]):
                stack_item = stack.pop()
                queue.append(stack_item)
            stack.append(line[i])

        i += 1

    while len(stack) > 0:
        queue.append(stack.pop())

    return queue


def evaluate_rpn(rpn):
    result_stack = list()
    for item in rpn:
        if item.lstrip("+-").isdigit():
            result_stack.append(item)
        else:
            right_operand = result_stack.pop()
            left_operand = result_stack.pop()
            result = float(eval(left_operand + item + right_operand))
            result_stack.append(str(result))
    return float(result_stack[0]) if len(result_stack) == 1 else "Error"


def main():
    while True:
        try:
            line = clean_line(input())
            #print(line)
            rpn_queue = convert_rpn(line)
            #print(rpn_queue)
            print(f"{evaluate_rpn(rpn_queue):.2f}")
            #print()
        except EOFError:
            break

if __name__ == "__main__":
    main()