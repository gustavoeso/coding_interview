def find_intersection(head1, head2,):
    ref1, ref2 = head1, head2

    while ref1 != ref2:
        ref1 = ref1.next
        ref2 = ref2.next

        if ref1 is None:
            ref1 = head2
        
        if ref2 is None:
            ref2 = head1
    
    return ref1