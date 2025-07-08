# Ask the user to enter a number
$number = Read-Host "Enter a number"
$number = [int]$number  # Convert input to integer

Write-Host "`nCounting down:"
for ($i = $number; $i -ge 0; $i--) {
    Write-Host $i
}

Write-Host "`nCounting up:"
for ($i = 0; $i -le $number; $i++) {
    Write-Host $i
}