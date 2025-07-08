$rand1 = Get-Random -Minimum 1 -Maximum 11
$rand2 = Get-Random -Minimum 1 -Maximum 51
$rand3 = Get-Random -Minimum 1 -Maximum 101

Write-Host "Choose a number range to guess from:"
Write-Host "1. 1 to 10"
Write-Host "2. 1 to 50"
Write-Host "3. 1 to 100"
$choice = Read-Host "Enter 1, 2, or 3"

switch ($choice) {
    "1" { $target = $rand1; $max = 10 }
    "2" { $target = $rand2; $max = 50 }
    "3" { $target = $rand3; $max = 100 }
    default {
        Write-Host "Invalid choice. Exiting."
        exit
    }
}

do {
    $input = Read-Host "Guess the number (1 to $max)"

    if (-not ($input -as [int])) {
        Write-Host "Please enter a valid number."
        continue
    }

    $guess = [int]$input

    if ($guess -lt $target) {
        Write-Host "Too low."
    } elseif ($guess -gt $target) {
        Write-Host "Too high."
    } else {
        Write-Host "Correct! The number was $target."
    }
}
until ($guess -eq $target)
