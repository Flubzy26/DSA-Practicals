#include <iostream>
#include <string.h>
#include <math.h>
#include <algorithm>
#define SIZE 50
using namespace std;

// ================= Stack Implementation Using Singly Linked List =================

struct Node {
    int data;
    Node* next;
};

Node* topNode = NULL;   // stack top pointer

// push onto stack
void push(int x) {
    Node* newNode = new Node();
    newNode->data = x;
    newNode->next = topNode;
    topNode = newNode;
}

// pop from stack
int pop() {
    if (topNode == NULL) {
        cout << "Stack Underflow!\n";
        return -1;
    }
    Node* temp = topNode;
    int val = temp->data;
    topNode = topNode->next;
    delete temp;
    return val;
}

// check if stack is empty
bool empty() {
    return (topNode == NULL);
}

// peek top element
int peek() {
    if (topNode == NULL) return -1;
    return topNode->data;
}

// ================= Utility Functions =================

bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

int precedence(char ch) {
    if (ch == '^')
        return 3;
    else if (ch == '*' || ch == '/')
        return 2;
    else if (ch == '+' || ch == '-')
        return 1;
    else
        return -1;
}

// ================= Infix → Postfix =================
void conversionPostfix(char infix[], char postfix[]) {
    int i, j = 0;
    for (i = 0; infix[i] != '\0'; i++) {
        if (isalpha(infix[i])) {
            postfix[j++] = infix[i];
        } else if (infix[i] == '(') {
            push(infix[i]);
        } else if (infix[i] == ')') {
            while (!empty() && peek() != '(') {
                postfix[j++] = pop();
            }
            pop(); // remove '('
        } else if (isOperator(infix[i])) {
            while (!empty() && precedence(infix[i]) <= precedence(peek())) {
                postfix[j++] = pop();
            }
            push(infix[i]);
        }
    }
    while (!empty()) {
        postfix[j++] = pop();
    }
    postfix[j] = '\0';
    cout << "\nPostfix Expression is: " << postfix << endl;
}

// ================= Infix → Prefix =================
void conversionPrefix(char infix[], char prefix[]) {
    int len = strlen(infix);
    reverse(infix, infix + len);

    for (int i = 0; i < len; i++) {
        if (infix[i] == '(') infix[i] = ')';
        else if (infix[i] == ')') infix[i] = '(';
    }

    int j = 0;
    for (int i = 0; i < len; i++) {
        if (isalpha(infix[i])) {
            prefix[j++] = infix[i];
        } else if (infix[i] == '(') {
            push(infix[i]);
        } else if (infix[i] == ')') {
            while (!empty() && peek() != '(') {
                prefix[j++] = pop();
            }
            pop();
        } else if (isOperator(infix[i])) {
            while (!empty() && precedence(infix[i]) <= precedence(peek())) {
                prefix[j++] = pop();
            }
            push(infix[i]);
        }
    }
    while (!empty()) {
        prefix[j++] = pop();
    }
    prefix[j] = '\0';
    reverse(prefix, prefix + j);
    cout << "\nPrefix Expression is: " << prefix << endl;
}

// ================= Postfix Evaluation =================
void evaluationPostfix(char postfix[]) {
    int ans, op1, op2, n;
    for (int i = 0; postfix[i] != '\0'; i++) {
        if (isalpha(postfix[i])) {
            cout << "\nEnter value for " << postfix[i] << ": ";
            cin >> n;
            push(n);
        } else if (isOperator(postfix[i])) {
            op2 = pop();
            op1 = pop();
            switch (postfix[i]) {
                case '+': ans = op1 + op2; break;
                case '-': ans = op1 - op2; break;
                case '*': ans = op1 * op2; break;
                case '/': ans = op1 / op2; break;
                case '^': ans = int(pow(op1, op2)); break;
            }
            push(ans);
        }
    }
    ans = pop();
    cout << "\nAnswer of the expression is: " << ans << endl;
}

// ================= Prefix Evaluation =================
void evaluationPrefix(char prefix[]) {
    int ans, op1, op2, n;
    int len = strlen(prefix);
    for (int i = len - 1; i >= 0; i--) {
        if (isalpha(prefix[i])) {
            cout << "\nEnter value for " << prefix[i] << ": ";
            cin >> n;
            push(n);
        } else if (isOperator(prefix[i])) {
            op1 = pop();
            op2 = pop();
            switch (prefix[i]) {
                case '+': ans = op1 + op2; break;
                case '-': ans = op1 - op2; break;
                case '*': ans = op1 * op2; break;
                case '/': ans = op1 / op2; break;
                case '^': ans = int(pow(op1, op2)); break;
            }
            push(ans);
        }
    }
    ans = pop();
    cout << "\nAnswer of the prefix expression is: " << ans << endl;
}

// ================= Main Function =================
int main() {
    int ch;
    char postfix[SIZE], prefix[SIZE], infix[SIZE], res;
    cout << "Enter the infix expression: ";
    cin >> infix;

    do {
        cout << "\n1: Conversion to Postfix\n2: Evaluation of Postfix\n";
        cout << "3: Conversion to Prefix\n4: Evaluation of Prefix\n";
        cout << "Enter your choice: ";
        cin >> ch;
        switch (ch) {
            case 1: conversionPostfix(infix, postfix); break;
            case 2: evaluationPostfix(postfix); break;
            case 3: conversionPrefix(infix, prefix); break;
            case 4: evaluationPrefix(prefix); break;
            default: cout << "Invalid choice" << endl;
        }
        cout << "Do you want to continue (y/n): ";
        cin >> res;
    } while (res == 'y' || res == 'Y');
    return 0;
}
