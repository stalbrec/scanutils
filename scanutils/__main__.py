import argparse
from pypdf import PdfReader, PdfWriter


def merge_alternating(front_pdf: str, back_pdf: str, output_pdf: str) -> None:
    front_reader = PdfReader(front_pdf)
    back_reader = PdfReader(back_pdf)

    writer = PdfWriter()

    n_front = len(front_reader.pages)
    n_back = len(back_reader.pages)

    if n_front != n_back:
        raise RuntimeError(
            f"Number of front pages ({n_front}) and back pages ({n_back}) must match!"
        )
    n_pages = n_front

    front_pages = list(front_reader.pages)
    back_pages = list(reversed(back_reader.pages))

    for i in range(n_pages):
        writer.add_page(front_pages[i])
        writer.add_page(back_pages[i])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"merged PDF written to {output_pdf}")


def main():
    parser = argparse.ArgumentParser(
        description="Merge two PDFs by interleaving their pages."
    )
    parser.add_argument("front_pdf", help="PDF containing front pages")
    parser.add_argument("back_pdf", help="PDF containing back pages")
    parser.add_argument(
        "-o",
        "--output",
        default="merged_output.pdf",
        help="Output file name (default: merged_output.pdf)",
    )

    args = parser.parse_args()

    merge_alternating(args.front_pdf, args.back_pdf, args.output)


if __name__ == "__main__":
    main()
