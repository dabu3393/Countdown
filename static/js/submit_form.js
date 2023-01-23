function submitForm() {
    event.preventDefault(); // prevent the form from refreshing the page

    // get the form data
    const event = document.forms["form"]["event"].value;
    const date = document.forms["form"]["date"].value;
    const time = document.forms["form"]["time"].value;

    // send the data to your Python script using fetch()
    fetch('countdown_clock.py', {
        method: 'POST',
        body: JSON.stringify({ event, date, time }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        // handle the response from the Python script
        console.log(data);
    });
}
