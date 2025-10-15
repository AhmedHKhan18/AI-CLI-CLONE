#!/usr/bin/env node
import { spawn } from "child_process";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Path to your Python script
const pythonScript = path.join(__dirname, "main.py");

// Spawn a Python process
const child = spawn("python", [pythonScript, ...process.argv.slice(2)], {
  stdio: "inherit",
});

child.on("close", (code) => {
  process.exit(code);
});
