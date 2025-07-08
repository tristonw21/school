# Ask Yes/No questions
$student = Read-Host "Are you a student at the university? (Yes/No)"
$graduating = Read-Host "Are you graduating this spring? (Yes/No)"
$gamer = Read-Host "Do you play video games? (Yes/No)"
$pets = Read-Host "Do you have any pets? (Yes/No)"
$breakfast = Read-Host "Is breakfast food better than other types of food? (Yes/No)"

Write-Host "`n--- Your Answers ---"

if ($student -match '^(yes|y)$') {
    Write-Host "Yes, you are a student."
} else {
    Write-Host "No, you are not a student."
}

if ($graduating -match '^(yes|y)$') {
    Write-Host "Yes, you are graduating this spring."
} else {
    Write-Host "No, you are not graduating this spring."
}

if ($gamer -match '^(yes|y)$') {
    Write-Host "Yes, you play video games."
} else {
    Write-Host "No, you don't play video games."
}

if ($pets -match '^(yes|y)$') {
    Write-Host "Yes, you have pets."
} else {
    Write-Host "No, you don't have pets."
}

if ($breakfast -match '^(yes|y)$') {
    Write-Host "Yes, breakfast is your favorite."
} else {
    Write-Host "No, you prefer other food types."
}
