// Sample data for national forests
const forests = [
  { id: 1, name: "Yosemite National Park" },
  { id: 2, name: "Yellowstone National Park" },
  { id: 3, name: "Grand Canyon National Park" },
  { id: 4, name: "Rocky Mountain National Park" },
  { id: 5, name: "Great Smoky Mountains National Park" },
];

// State to track liked locations
let likedLocations = [];

// Function to render the list of forests
function renderForests() {
  const forestList = document.getElementById("forests");
  forestList.innerHTML = "";

  forests.forEach((forest) => {
    const li = document.createElement("li");
    li.textContent = forest.name;

    const likeButton = document.createElement("button");
    likeButton.textContent = "Like";
    likeButton.onclick = () => likeForest(forest);

    li.appendChild(likeButton);
    forestList.appendChild(li);
  });
}

// Function to render the liked locations
function renderLikedLocations() {
  const likedList = document.getElementById("liked");
  likedList.innerHTML = "";

  likedLocations.forEach((location) => {
    const li = document.createElement("li");
    li.textContent = location.name;
    likedList.appendChild(li);
  });
}

// Function to handle liking a forest
function likeForest(forest) {
  if (!likedLocations.some((location) => location.id === forest.id)) {
    likedLocations.push(forest);
    renderLikedLocations();
  }
}

// Initial render
renderForests();
renderLikedLocations();