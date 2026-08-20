from enum import IntEnum, auto
from rich import print as rich_print

class DebugLevel(IntEnum):
  QUIET = auto()
  ERRORS = auto()
  WARNINGS = auto()
  INFO = auto()

debug_level: DebugLevel = DebugLevel.INFO

def rich_print_by_debug(
    debug_level: DebugLevel,
    string: str,
    *args, **kwargs) -> None:
  
  match debug_level:
    case DebugLevel.QUIET:
      return
    case DebugLevel.ERRORS:
      rich_print(
        f"[bold red]Error: {string}[/bold red]",
        *args, **kwargs
      )
    case DebugLevel.WARNINGS:
      rich_print(
        f"[italic yellow]Warning: {string}[/italic yellow]",
        *args, **kwargs
      )
    case DebugLevel.INFO:
      rich_print(
        f"[italic]Info: {string}[/italic]",
        *args, **kwargs
      )

def print_if_debug(
    required_debug: DebugLevel,
    string: str,
    *args, **kwargs) -> bool:
  if debug_level < required_debug:
    return False
  
  rich_print_by_debug(required_debug, string, *args, **kwargs)
  return True

def main() -> None:
  print_if_debug(DebugLevel.ERRORS, "meow")

if __name__ == "__main__":
  main()