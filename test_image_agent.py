from image_agent import analyze_image


print("=" * 60)
print("       CLIMATEGUARD AI - IMAGE TEST")
print("=" * 60)

image_path = input("\nEnter the full path of an image: ")

try:

    result = analyze_image(image_path)

    print("\n" + "=" * 60)
    print("       IMAGE ANALYSIS")
    print("=" * 60)

    print(result)

    print("\n" + "=" * 60)
    print("IMAGE TEST COMPLETE")
    print("=" * 60)

except Exception as e:

    print("\nERROR:")
    print(e)