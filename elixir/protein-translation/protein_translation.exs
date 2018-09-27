defmodule ProteinTranslation do

  @codons %{
    "UGU" => "Cysteine",
    "UGC" => "Cysteine",
    "UUA" => "Leucine",
    "UUG" => "Leucine",
    "AUG" => "Methionine",
    "UUU" => "Phenylalanine",
    "UUC" => "Phenylalanine",
    "UCU" => "Serine",
    "UCC" => "Serine",
    "UCA" => "Serine",
    "UCG" => "Serine",
    "UGG" => "Tryptophan",
    "UAU" => "Tyrosine",
    "UAC" => "Tyrosine",
    "UAA" => "STOP",
    "UAG" => "STOP",
    "UGA" => "STOP",
  }

  def of_rna(rna) do
    proteins = get_proteins(String.graphemes(rna))
    cond do
      Enum.member?(proteins, "error") -> {:error, "invalid RNA"}
      true -> {:ok, proteins}
    end
  end

  defp get_proteins([]), do: []
  defp get_proteins([a, b, c | tail]) do
    protein = @codons[a <> b <> c]
    case protein do
      nil -> ["error"]
      "STOP" -> []
      p -> [p | get_proteins(tail)]
    end
  end

  def of_codon(codon) do
    protein = @codons[codon]
    case protein do
      nil -> {:error, "invalid codon"}
      _ -> {:ok, protein}
    end
  end
end
