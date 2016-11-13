import config
import handler


def main():
    tokenKey = config.ConfigSectionMap('CONFIG')['token']
    handler.Handler(tokenKey)

if __name__ == '__main__':
    main()
