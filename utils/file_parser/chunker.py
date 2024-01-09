from typing import Union, List
import logging


def chunk_text_by_num_words(
    source_text: str, max_chunk_words: int = 100, overlap_fraction: float = 0.15
) -> List[str]:
    """
    Chunk text input into a list of strings, using a number of words
    :param source_text: Input string to be chunked
    :param max_chunk_words: Maximum length of chunk, in words
    :param overlap_fraction: Overlap as a percentage of chunk_words. The overlap is prepended to each chunk.
    :return: return a list of words
    """
    logging.info(f"Chunking text of {len(source_text)} chars by number of words.")
    sep = " "
    overlap_words = int(max_chunk_words * overlap_fraction)

    source_text = source_text.strip()
    word_list = source_text.split(sep)
    chunks_list = list()

    n_chunks = ((len(word_list) - 1 + overlap_words) // max_chunk_words) + 1
    for i in range(n_chunks):
        window_words = word_list[
            max(max_chunk_words * i - overlap_words, 0) : max_chunk_words * (i + 1)
        ]
        chunks_list.append(sep.join(window_words))
    return chunks_list


def remove_multiple_whitespaces(source_text: str) -> str:
    """
    Replace multiple whitespaces with single space
    :param source_text:
    :return:
    """
    import re

    source_text = re.sub(r"\s+", " ", source_text)
    return source_text


def chunk_text(source_text: str) -> List[str]:
    """
    Chunk longer text
    :param source_text:
    :return:
    """
    logging.info(f"Chunking text of {len(source_text)} characters.")
    source_text = remove_multiple_whitespaces(source_text)
    return chunk_text_by_num_words(source_text)
