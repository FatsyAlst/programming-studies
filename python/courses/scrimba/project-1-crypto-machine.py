# ===================================
# ENIGMA LIGHT - CRYPTO MACHINE PROJECT
# ===================================
# Scrimba Python 101 Course - Project 1
# A simple Caesar cipher implementation using dictionary-based character substitution

print('Project - Crypto')

# ===================================
# MAIN FUNCTION: ENIGMA_LIGHT
# ===================================

def enigma_light():
    """
    Encrypts or decrypts messages using a simple substitution cipher.
    
    How it works:
    1. Creates a mapping where each character shifts by one position
    2. The last character wraps around to become the first
    3. Uses two dictionaries: one for encoding, one for decoding
    
    Returns:
        str: The encoded or decoded message (capitalized)
    """
    
    # ===================================
    # STEP 1: CREATE CHARACTER MAPPING
    # ===================================
    # Original alphabet with space and exclamation mark
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    
    # Shifted alphabet: last character moves to front, rest shift right
    # keys[-1] gets '!', keys[0:-1] gets 'abcdefghijklmnopqrstuvwxyz '
    # Result: '!abcdefghijklmnopqrstuvwxyz '
    values = keys[-1] + keys[0:-1]
    
    # Example mapping:
    # 'a' -> '!'
    # 'b' -> 'a'
    # 'c' -> 'b'
    # ...
    # ' ' -> 'y'
    # '!' -> 'z'
    
    
    # ===================================
    # STEP 2: CREATE ENCODING/DECODING DICTIONARIES
    # ===================================
    # Encoding dictionary: maps original character to encoded character
    dict_e = dict(zip(keys, values))
    # Example: {'a': '!', 'b': 'a', 'c': 'b', ..., '!': 'z'}
    
    # Decoding dictionary: reverse mapping (values become keys)
    dict_d = {value: key for key, value in dict_e.items()}
    # Example: {'!': 'a', 'a': 'b', 'b': 'c', ..., 'z': '!'}
    
    
    # ===================================
    # STEP 3: GET USER INPUT
    # ===================================
    msg = input("Enter your secret message quietly: ")
    mode = input('Crypto mode: encode (e) OR decode (d): ')
    
    
    # ===================================
    # STEP 4: ENCODE OR DECODE MESSAGE
    # ===================================
    if mode.lower() == 'e':
        # Encoding: Convert each letter using dict_e
        # List comprehension iterates through each character
        # Joins all encoded characters into single string
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        # Decoding: Convert each letter using dict_d (reverse mapping)
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    
    # ===================================
    # STEP 5: RETURN RESULT
    # ===================================
    # Capitalize first letter for presentation
    return new_msg.capitalize()


# ===================================
# PROGRAM EXECUTION
# ===================================
print(enigma_light())


# ===================================
# EXAMPLE USAGE
# ===================================
# Input:  "hello world!"
# Mode:   encode (e)
# Output: "Gdkkn vnqkc "
#
# Input:  "gdkkn vnqkc "
# Mode:   decode (d)
# Output: "Hello world!"


# ===================================
# CONCEPTS USED IN THIS PROJECT
# ===================================
# 1. String slicing - keys[-1], keys[0:-1]
# 2. zip() - Combining two sequences
# 3. dict() - Creating dictionary from zip
# 4. Dictionary comprehension - {value: key for key, value in dict.items()}
# 5. input() - Getting user input
# 6. str.lower() - Converting to lowercase
# 7. List comprehension - [dict_e[letter] for letter in msg.lower()]
# 8. str.join() - Combining list of characters into string
# 9. str.capitalize() - Formatting output
# 10. Conditional logic - if/else for mode selection
# 11. Dictionary lookup - dict_e[letter], dict_d[letter]
# 12. Functions - Encapsulating logic in enigma_light()


# ===================================
# HOW THE CIPHER WORKS
# ===================================
# This is a simple substitution cipher (Caesar cipher variant)
# 
# Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z   !
# Encoded:   ! a b c d e f g h i j k l m n o p q r s t u v w x y z  
#
# Each character shifts one position to the left (with wraparound)
# The encoding and decoding are inverse operations


# ===================================
# SECURITY NOTE
# ===================================
# This cipher is NOT secure for real cryptography!
# It's vulnerable to:
# - Frequency analysis (common letters like 'e' stand out)
# - Known plaintext attacks
# - Brute force (only 28 possible shifts to try)
#
# For real security, use proper encryption libraries like:
# - cryptography module
# - hashlib for hashing
# - secrets module for secure random generation


# ===================================
# FUTURE IMPROVEMENT CHALLENGES
# ===================================

# CHALLENGE 1: ERROR HANDLING
# ----------------------------
# Goal: Make the program more robust
# Tasks:
# - Handle characters not in the keys string (numbers, special chars)
# - Validate mode input (only accept 'e' or 'd')
# - Add try-except for KeyError when character not found
# - Give user option to retry on invalid input
# - Handle empty message input
# Skills practiced: Exception handling, input validation, defensive programming

# CHALLENGE 2: ENHANCED CIPHER STRENGTH
# --------------------------------------
# Goal: Make the cipher harder to crack
# Tasks:
# - Implement variable shift amount (user chooses shift size)
# - Add support for numbers and more special characters
# - Implement random shuffling instead of simple shift
# - Create multi-layer encoding (encode result again with different key)
# - Add salt or key-based encoding
# Skills practiced: Algorithm design, randomization, cryptography concepts

# CHALLENGE 3: FILE OPERATIONS
# -----------------------------
# Goal: Encode/decode entire files
# Tasks:
# - Read message from text file instead of user input
# - Save encoded/decoded result to output file
# - Support batch processing (multiple files)
# - Preserve file format (newlines, punctuation)
# - Add command-line arguments for file paths
# Skills practiced: File I/O, command-line arguments, batch processing

# CHALLENGE 4: IMPROVED USER INTERFACE
# -------------------------------------
# Goal: Make the program more user-friendly
# Tasks:
# - Create menu system (encode, decode, quit)
# - Show encoded alphabet before asking for message
# - Display character count and processing time
# - Add "copy to clipboard" option for results
# - Create colorful terminal output with ANSI codes
# Skills practiced: User interface design, menu systems, terminal formatting

# CHALLENGE 5: MULTIPLE CIPHER METHODS
# -------------------------------------
# Goal: Support different encryption techniques
# Tasks:
# - Implement Caesar cipher with variable shift
# - Add Vigenère cipher (keyword-based)
# - Implement ROT13 encoding
# - Add Atbash cipher (reverse alphabet)
# - Let user choose cipher type from menu
# Skills practiced: Multiple algorithms, algorithm selection, modular design

# CHALLENGE 6: KEY MANAGEMENT
# ----------------------------
# Goal: Add password/key protection
# Tasks:
# - Require password to encode/decode
# - Generate cipher key from password (hash-based)
# - Save encrypted keys to file
# - Implement key expiration dates
# - Add "change password" functionality
# Skills practiced: Password handling, key derivation, security concepts

# CHALLENGE 7: REVERSE ENGINEERING PROTECTION
# --------------------------------------------
# Goal: Make encoded messages harder to decode without key
# Tasks:
# - Implement custom character mapping (not simple shift)
# - Add dummy characters to confuse analysis
# - Implement polyalphabetic substitution
# - Add checksum to detect tampering
# - Obfuscate the encoding pattern
# Skills practiced: Advanced cryptography, pattern obfuscation

# CHALLENGE 8: ANALYSIS TOOLS
# ----------------------------
# Goal: Create tools to analyze encoded messages
# Tasks:
# - Calculate letter frequency in encoded message
# - Compare against English letter frequency
# - Implement brute force decoder (try all shifts)
# - Create dictionary attack (try common words)
# - Visualize frequency distribution with ASCII charts
# Skills practiced: Data analysis, statistics, visualization

# CHALLENGE 9: OBJECT-ORIENTED DESIGN
# ------------------------------------
# Goal: Restructure using classes
# Tasks:
# - Create Cipher base class with encode/decode methods
# - Create CaesarCipher, VigenereCipher subclasses
# - Implement Message class with text and metadata
# - Create CipherKey class for key management
# - Use composition and inheritance appropriately
# Skills practiced: OOP, inheritance, polymorphism, design patterns

# CHALLENGE 10: GUI VERSION
# --------------------------
# Goal: Create graphical interface
# Tasks:
# - Build GUI with tkinter
# - Add text boxes for input/output
# - Include encode/decode buttons
# - Show real-time character-by-character encoding
# - Add "load file" and "save file" dialogs
# Skills practiced: GUI programming, event handling, user experience

# CHALLENGE 11: TESTING SUITE
# ----------------------------
# Goal: Ensure code reliability
# Tasks:
# - Write unit tests for encode/decode functions
# - Test with edge cases (empty string, special chars)
# - Verify encode→decode returns original message
# - Test all cipher variants
# - Create performance benchmarks for different message sizes
# Skills practiced: Unit testing, test-driven development, edge cases

# CHALLENGE 12: DOCUMENTATION & PACKAGING
# ----------------------------------------
# Goal: Make project professional and shareable
# Tasks:
# - Add comprehensive docstrings to all functions
# - Create README.md with usage examples
# - Add type hints throughout code
# - Follow PEP 8 style guide strictly
# - Package as installable module with setup.py
# Skills practiced: Documentation, type hints, packaging, Python standards

# BONUS CHALLENGE: REAL ENCRYPTION
# ---------------------------------
# Goal: Implement actual secure encryption
# Tasks:
# - Use Python's cryptography library (Fernet)
# - Implement AES encryption properly
# - Add secure key generation and storage
# - Implement digital signatures for authenticity
# - Learn about and implement proper IV/salt usage
# Skills practiced: Real cryptography, security best practices, industry standards