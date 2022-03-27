# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:47:27 2022

@author: dejong71
"""

#------------------------------------------------------------------------------

class Category:
    def __init__(self, name):
        self.name = name.capitalize()
        self.ledger = []
        
    #--------------------------------------------------------------------------
    
    def get_balance(self):
        '''
        Get the current balance of the ledger.
        '''
        return sum(x['amount'] for x in self.ledger)
    
    #--------------------------------------------------------------------------

    def check_funds(self, amount):
        '''
        Check if the current ledger balance is larger than an amount.
        '''
        return self.get_balance() >= amount
    
    #--------------------------------------------------------------------------

    def deposit(self, amount, description=''):
        '''
        Deposit an amount into the ledger.
        '''
        self.ledger.append({'amount': amount,
                            'description': description})
        
    #--------------------------------------------------------------------------

    def withdraw(self, amount, description=''):
        '''
        Withdraw an amount from the ledger, if sufficient funds are available.
        '''
        check = self.check_funds(amount)
        if check:
            self.ledger.append({'amount': - amount, 'description': description})
        return check

    #--------------------------------------------------------------------------

    def transfer(self, amount, other):
        '''
        Transfer an amount between ledgers, if sufficient funds are available.
        '''
        check = self.check_funds(amount)
        if check:
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
        return check
    
    #--------------------------------------------------------------------------
    
    def _format_title(self, line=30):
        '''
        Hidden method to build up the __repr__ title.
        '''
        n = self.name
        n_stars = int((line - len(n))/2)
        title = n_stars * '*' + n + n_stars * '*'
        if len(n) % 2 != 0:
            title += '*'
        return title
    
    #--------------------------------------------------------------------------
    
    def _format_line(self, item, line=30, w_price=7):
        '''
        Hidden method to build up the __repr__ lines.
        '''
        w_descr = line - w_price
        d = f'{item["description"]:{w_descr}}'
        if len(d) > w_descr:
            d = d[:w_descr]
        p = f'{item["amount"]:>{w_price}.2f}'
        if len(p) > w_price:
            p = p[-w_price:]
        return d + p
    #--------------------------------------------------------------------------
    
    def __repr__(self):
        string = '' + self._format_title() + '\n'
        for item in self.ledger:
            string += self._format_line(item) + '\n'
        string += f'Total: {self.get_balance():.2f}'
        return string

#------------------------------------------------------------------------------

def get_relative_spend(categories):
    '''
    Construct a dictionary of the relative spends of each category, rounded 
    down to the nearest 10.
    '''
    spends = {}
    total_spent = 0
    for cat in categories:
        cost = sum(i['amount'] for i in cat.ledger if i['amount'] < 0)
        spends[cat.name] = cost
        total_spent += cost
    rel_spends = {cat: (100 * spends[cat]/total_spent) // 10 * 10 
                  for cat in spends}
    return rel_spends

#------------------------------------------------------------------------------

def create_spend_chart(categories):
    '''
    The graph is constructed from a dictionary with the y-value as key and the 
    associated line as value. For each position on the x-axis, the line is 
    extended by an 'o' (if the value is above that y-value) or a ' ' (if the 
    value is below the y-value).
    
    Interleave all x-tick labels. Take a slice equally long as the amount of 
    x-ticks and seperate the characters in that slice by 2 ' '. Add to the 
    text. Remove the final newline character but keep the trailing spaces.
    '''
    spends = get_relative_spend(categories)
    yvals = {i: '' for i in range(100, -1, -10)}
    text = 'Percentage spent by category\n'
    for yval in yvals:
        text += f'{yval:3}| '
        for cat in categories:
            if spends[cat.name] >= yval:
                text += 'o  '
            else:
                text += '   '
        text += '\n'
    text += ' ' * 4 + '---' * len(categories) + '-\n'
    
    x_tick_length = max( (len(x.name) for x in categories) )
    x_ticks = [ f'{x.name:{x_tick_length}}' for x in categories ]
    
    
    mixed = ''.join(i for j in zip(*x_ticks) for i in j)
    for i in range(0, len(x_ticks) * x_tick_length, len(x_ticks)):
        text += ' ' * 5 +  '  '.join(mixed[i : i + len(x_ticks)]) + '  \n'
    
    return text.strip('\n')

#------------------------------------------------------------------------------