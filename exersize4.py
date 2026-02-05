###########################Exersize 4.1###############################
class SequenceAnalyzer:
    """A comprehensive DNA sequence analysis tool."""
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def calculate_gc_content(self):
        """
        Calculate the GC content of a DNA sequence.
    
        Parameters:
        dna_sequence (str): DNA sequence containing A, T, G, C
    
        Returns:
        float: GC content as a percentage
        """
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        total_length = len(self.sequence)
        gc_content = (gc_count / total_length) * 100
        return gc_content

    def count_nucleotides(self):
        """
        Count occurrences of each nucleotide in a DNA sequence.
    
        Parameters:
        dna_sequence (str): DNA sequence
    
        Returns:
        dict: Dictionary with nucleotide counts
        """
    # Your code here
        amountA = self.sequence.count('A')
        amountT = self.sequence.count('T')
        amountG = self.sequence.count('G')
        amountC = self.sequence.count('C')
        counted_nucleotides = {'A':amountA, 'T':amountT, 'G':amountG, 'C':amountC }
        return counted_nucleotides
    
    def Transcribe(self):
        return self.sequence.replace("T", "U")

    def Reverse(self):
        Reverse_compliment = ""
        for i in self.sequence:
            if i == "T":
                Reverse_compliment += "A"
            if i == "A":
                Reverse_compliment += "T"
            if i == "C": 
                Reverse_compliment += "G"
            if i == "G":
                Reverse_compliment += "C"
        return Reverse_compliment 
    
    def generate_report(self):
        report = "=" * 50 + "\n"
        report += "DNA Sequence Analysis Report\n"
        report += "=" * 50 + "\n\n"

        report += f"Sequence: {self.sequence}\n"
        report += f"GC content: {self.calculate_gc_content()} \n"
        report += f"Nucleotides: {self.count_nucleotides()} \n"
        report += f"Transcibed RNA: {self.Transcribe()} \n"
        report += f"Reverse compliment: {self.Reverse()} \n"

        report += "\n"+ "=" * 50

        return report
    pass

# Test your class

seq = SequenceAnalyzer("ATGCGATCGATCGTAGCTA")
#print(seq)
#print(seq.calculate_gc_content())
#print(seq.Transcribe())
#print(seq.Reverse())
print(seq.generate_report())