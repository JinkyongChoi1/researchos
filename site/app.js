const stages = [
  ["capture", "Question captured"], ["plan", "Plan + falsifier"], ["research", "Sources attached"],
  ["critique", "Risks surfaced"], ["decide", "Human gate"], ["log", "Provenance saved"], ["resume", "Ready to resume"]
];
document.getElementById("timeline").innerHTML = stages.map(([name, note], i) => `<div class="step done ${name === "decide" ? "human" : ""}"><b>${i + 1}. ${name}</b><small>${note}</small></div>`).join("");
