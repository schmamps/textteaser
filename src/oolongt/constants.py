from pathlib import Path

from .typedefs import STR_LIST  # noqa

# summarizer
DEFAULT_LENGTH = 5
TOP_KEYWORD_MIN_RANK = 10

# approximation
COMPOSITE_TOLERANCE = 0.000000000001  # composite scores

# parser
BUILTIN = str(Path(__file__).parent.joinpath('idioms'))  # type: str
DEFAULT_IDIOM = 'default'
DEFAULT_IDEAL_LENGTH = 20
DEFAULT_LANGUAGE = 'english'
DEFAULT_NLTK_STOPS = True
DEFAULT_USER_STOPS = []   # type: STR_LIST

# scored keyword
KEYWORD_SCORE_K = 1.5
