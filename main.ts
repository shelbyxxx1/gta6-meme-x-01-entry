import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoDir = path.dirname(fileURLToPath(import.meta.url));
const source = path.join(repoDir, "POST.json");
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const destination = path.join(outputDir, "POST.json");

fs.mkdirSync(outputDir, { recursive: true });
const contents = fs.readFileSync(source);
fs.writeFileSync(destination, contents);
console.log("copied POST.json (" + contents.length + " bytes) to " + destination);
