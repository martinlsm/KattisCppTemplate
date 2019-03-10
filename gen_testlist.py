import os

if __name__ == '__main__':
    tests = [f[:-3] for f in os.listdir('test/') if f.endswith('.in')]
    tests.sort()
    with open('testlist', 'w') as f:
        for t in tests:
            f.write(t + '\n')
