from django import template

import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

register = template.Library()

# pygmentize -S default -f html -a .highlight > default.css
# pygmentize -S monokai -f html -a .highlight > pygment.css
"""
/* fix bootstrap conflict with Pygments */
.highlight pre {
    white-space: pre;
    border-radius: inherit;
    display: inherit;
    background-color: inherit;
    border: inherit;
    color: inherit;
  }

/* fix conflict with other sytlesheets */
.highlight .m { margin: inherit; }
"""
class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(value)


# renderer = HighlightRenderer()
# markdown = mistune.Markdown(renderer=renderer)
