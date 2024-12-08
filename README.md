# Memory-Allocation-Algorithm

<h2>1. Quick Fit Memory Algorithm</h2>

This is a Python-based application demonstrating memory allocation using the Quick Fit algorithm. This application works as a memory allocation simulator. It shows how the Quick Fit algorithm process works. It provides a graphical user interface (GUI) for users to allocate memory blocks, display free memory lists, and manage leftover memory efficiently.

<h3>Features</h3>

- **Graphical Interface**: User-friendly GUI built with PyQt5.
- **Quick Fit Algorithm**: Implements a memory allocation strategy that minimizes fragmentation.
- **Dynamic Free Lists**: Displays and updates memory blocks in real-time.
- **Error Handling**: Validates user input and handles edge cases gracefully.
- Each memory block is considered indivisible for a single process.
  
<h3>Assumptions</h3> 

- Each memory block is considered indivisible for a single process.
- Leftover memory from an allocation is immediately categorized as a new block if unused.
- If there are no suitable memory blocks in the list, it uses the best-fit algorithm to allocate a suitable memory block. (The best-fit algorithm selects the smallest memory block that can accommodate the process size.)
  
<h3>Limitations</h3>  

- Memory block categories are pre-defined; dynamic resizing is not supported.
- Designed for educational purposes; not suitable for production use.
- <h3>Limitations</h3>


<h3>How It Works</h3>

1. The program maintains an initial list of memory blocks categorized by size.
   - 50KB, 100KB, 200KB, and 500KB, each with 10 blocks.
2. Users can allocate memory by entering a process size in KB.
3. The program uses the best-fit strategy to allocate the most appropriate memory block.
4. Leftover memory is added as a new block category if applicable.
5. Users can view the updated memory list after each allocation.

<h3>Requirements</h3>

- **Python 3.8+**
- **PyQt5**

<h3>Installation</h3>

1. Clone the repository or download the source code:
   ```bash
    git clone https://github.com/IreshaMadhuwanthi/Memory-Allocation-Algorithm.git
    cd Memory-Allocation-Algorithm
2. Install the required dependencies:
    ```bash
    pip install pyqt5

<h3>Usage</h3>

1. Run the program:
2. Enter the process size in the input field.
3. Click "Allocate" to allocate memory for the process.
4. Click "Show Lists" to view the current free memory blocks.

Example
   - Initial Free Memory Blocks:
       - 50KB List: 10 Blocks
       - 100KB List: 10 Blocks
       - 200KB List: 10 Blocks
       - 500KB List: 10 Blocks

   - After allocating 80KB:
       - Allocated from 100KB list. 9 out of 10 blocks left.
       - Created a new block list for 20KB leftover.

   - Updated Free Memory Blocks:
       - 20KB List: 1 Block
       - 50KB List: 10 Blocks
       - 100KB List: 9 Blocks
       - 200KB List: 10 Blocks
       - 500KB List: 10 Blocks
     
<h3>Future Enhancements</h3>

- Add functionality to deallocate memory and return it to the free list.
- Provide visual graphs to represent memory allocation and fragmentation.
- Enable custom block sizes and numbers via user input.

