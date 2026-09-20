from document_agent import analyze_document


print("=" * 60)
print("       CLIMATEGUARD AI - DOCUMENT AI TEST")
print("=" * 60)


pdf_path = input("\nEnter the full path of a PDF: ")


try:

    print("\nReading document...")

    result = analyze_document(pdf_path)

    print("\n" + "=" * 60)
    print("       CLIMATEGUARD AI ANALYSIS")
    print("=" * 60)

    print("\n")
    print(result)

    print("\n" + "=" * 60)
    print("DOCUMENT AI ANALYSIS COMPLETE")
    print("=" * 60)


except Exception as e:

    print("\nERROR:")
    print(e)