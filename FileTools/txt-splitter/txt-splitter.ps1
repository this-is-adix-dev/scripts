[CmdletBinding()]
param (
    [Parameter(Mandatory)][string]$FilePath,
    [int]$LinesPerChunk = 500000,
    [int]$ChunkCount = 50,
    [string]$OutputPrefix = "part_",
    [string]$OutputSuffix = ".txt",
    [string]$OutputDirectory = ".",
    [string]$Encoding = "UTF8"
)

if (-not (Test-Path $OutputDirectory)) {
    New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}

$encoding = [System.Text.Encoding]::GetEncoding($Encoding)
$reader = [System.IO.StreamReader]::new($FilePath, $encoding)

try {
    for ($i = 0; $i -lt $ChunkCount; $i++) {
        $outFile = Join-Path $OutputDirectory "$OutputPrefix$i$OutputSuffix"
        $writer = [System.IO.StreamWriter]::new($outFile, $false, $encoding)

        try {
            $written = 0
            while ($written -lt $LinesPerChunk) {
                $line = $reader.ReadLine()
                if ($null -eq $line) { break }
                $writer.WriteLine($line)
                $written++
            }
        } finally {
            $writer.Close()
        }

        Write-Verbose "Wrote $written lines to $outFile"

        if ($null -eq $line) { break }
    }
} finally {
    $reader.Close()
}
