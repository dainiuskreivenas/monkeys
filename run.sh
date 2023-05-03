mkdir -p tests/results

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHONPATH="${PYTHONPATH};:${SCRIPT_DIR}/rbs"

python3 -m tests.Monkey_SingleFruit > ./tests/results/Monkey_SingleFruit.sp

python3 -m tests.Monkey_SingleWithChair > ./tests/results/Monkey_SingleWithChair.sp

python3 -m tests.Monkey_TwoFruits > ./tests/results/Monkey_TwoFruits.sp

python3 -m tests.Monkey_TwoPlaceFruits > ./tests/results/Monkey_TwoPlaceFruits.sp

python3 -m tests.Monkey_TwoSameFruits > ./tests/results/Monkey_TwoSameFruits.sp

python3 -m tests.Monkey_TwoSamePlaceFruits > ./tests/results/Monkey_TwoSamePlaceFruits.sp

python3 -m quillianYes -> ./tests/results/quillian.sp