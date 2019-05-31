#!/usr/bin/python3


# def tag(tag, *args, **kwargs):

#     if 'html_class' in kwargs:
#         kwargs['class'] = kwargs['html_class']
#         del kwargs['html_class']

#     attrs = "" if not kwargs else \
#         ''.join(f' {key}="{value}"' for key, value in kwargs.items())
#     output = f'<{tag}{attrs}>'

#     output += "".join(child for child in args) + f'</{tag}>'

#     return output


def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')

    attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert'
            )
    )
